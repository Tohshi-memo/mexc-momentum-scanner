# Decision Report

- generated_at: 2026-06-22T08:42:54.870540+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7357, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.75% | **-0.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +1.67% | **+0.50%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_BB3S | 8/19 | 42.1% | +1.04% | **+0.44%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.24% | **+2.24%** |
| MARKET_LONG | 20/20 | 100.0% | +2.13% | **+2.13%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.83% | **+1.19%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +0.89% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.95** / 初期 $100.00 (+1.95%)
- 確定トレード: 26件 (TP 10 / SL 16 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.95
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$229.45** / 初期 $100.00 (+129.45%)
- 確定: 2033件 (Win 599 / Loss 669 / Flat 765) / skip 1885件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $229.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 456件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0577 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T08:42:48.026992+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64165.1
- Funnel: target 801 → liquid 150 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +72.91% | $8,512,029.03 |
| UB/USDT:USDT | +31.01% | $13,330,919.14 |
| CLO/USDT:USDT | +26.36% | $3,741,797.47 |
| ZEST/USDT:USDT | +26.25% | $2,119,419.06 |
| O/USDT:USDT | +20.48% | $2,101,694.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.92% | +4.95% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.00% | +2.04% |
| W/USDT:USDT | below_1h_threshold | +1.35% | +1.39% |
| ENA/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| UAI/USDT:USDT | below_1h_threshold | +1.23% | +1.27% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
