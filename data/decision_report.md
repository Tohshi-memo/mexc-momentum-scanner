# Decision Report

- generated_at: 2026-06-27T00:25:41.130036+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7655**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7655, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.38% | **-1.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 5/14 | 35.7% | +1.90% | **+0.68%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.19% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.12% | **+1.25%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.85% | **+1.02%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.61% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.21** / 初期 $100.00 (+131.21%)
- 確定: 2180件 (Win 649 / Loss 725 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $231.21

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.68** / 初期 $100.00 (+7.68%)
- 確定: 387件 (Win 104 / Loss 100 / Flat 183) / skip 679件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0323 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGLD/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.68

## 5. Latest Market Context

- 更新: 2026-06-27T00:25:34.064991+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=60021.6
- Funnel: target 806 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.3 >= 65=1, 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +32.07% | $2,226,463.76 |
| AGLD/USDT:USDT | +19.65% | $5,359,670.86 |
| NES/USDT:USDT | +10.55% | $2,220,774.75 |
| VELVET/USDT:USDT | +10.44% | $28,196,680.93 |
| LAB/USDT:USDT | +6.39% | $24,238,456.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +2.88% | +2.96% |
| VELVET/USDT:USDT | below_1h_threshold | +2.88% | +2.96% |
| LAB/USDT:USDT | below_1h_threshold | +2.04% | +2.12% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.55% | +1.64% |
| RENDER/USDT:USDT | below_1h_threshold | +0.96% | +1.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
