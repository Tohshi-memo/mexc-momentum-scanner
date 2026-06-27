# Decision Report

- generated_at: 2026-06-27T00:52:58.086376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7660**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7660, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.17% | **-1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_BB3S | 5/16 | 31.2% | +2.00% | **+0.62%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.32% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.47% | **+0.99%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.68% | **+0.84%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$234.61** / 初期 $100.00 (+134.61%)
- 確定: 2185件 (Win 652 / Loss 727 / Flat 806) / skip 2036件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PUNDIX/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $234.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.83** / 初期 $100.00 (+7.83%)
- 確定: 391件 (Win 106 / Loss 100 / Flat 185) / skip 680件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PUNDIX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.83

## 5. Latest Market Context

- 更新: 2026-06-27T00:52:50.749297+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=60032.9
- Funnel: target 806 → liquid 164 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 85.8 >= 65=1, 4h RSI 76.9 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +42.31% | $2,900,680.56 |
| AGLD/USDT:USDT | +27.50% | $6,245,399.18 |
| VELVET/USDT:USDT | +12.79% | $28,754,974.32 |
| SLX/USDT:USDT | +11.47% | $10,626,280.89 |
| NES/USDT:USDT | +10.16% | $2,235,316.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.53% | +4.59% |
| MYX/USDT:USDT | below_1h_threshold | +4.26% | +4.32% |
| RENDER/USDT:USDT | below_1h_threshold | +2.23% | +2.29% |
| LAB/USDT:USDT | below_1h_threshold | +2.11% | +2.17% |
| BILL/USDT:USDT | below_1h_threshold | +1.46% | +1.53% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
