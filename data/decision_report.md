# Decision Report

- generated_at: 2026-06-27T00:17:16.154212+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7653**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7653, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.98% | **-1.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_BB3S | 5/13 | 38.5% | +1.90% | **+0.73%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.19% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.13% | **+1.45%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +3.50% | **+1.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.43% | **+1.22%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.53% | **+1.15%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.18% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.22** / 初期 $100.00 (+131.22%)
- 確定: 2178件 (Win 648 / Loss 724 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000385 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGLD/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $231.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 386件 (Win 103 / Loss 100 / Flat 183) / skip 678件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0299 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-27T00:17:10.267629+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=60075.3
- Funnel: target 806 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGLD/USDT:USDT | +14.71% | $5,139,351.45 |
| NES/USDT:USDT | +12.51% | $2,200,281.58 |
| PUNDIX/USDT:USDT | +10.97% | $2,024,518.87 |
| VELVET/USDT:USDT | +10.54% | $28,084,072.15 |
| ARX/USDT:USDT | +6.71% | $2,509,595.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.05% | +3.05% |
| USELESS/USDT:USDT | below_1h_threshold | +2.03% | +2.02% |
| ARX/USDT:USDT | below_1h_threshold | +1.91% | +1.90% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.62% | +1.62% |
| PUNDIX/USDT:USDT | below_1h_threshold | +1.34% | +1.33% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
