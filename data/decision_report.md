# Decision Report

- generated_at: 2026-06-20T01:48:33.182515+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7193**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7193, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +1.02% | **+0.91%** |
| LIMIT_BB3S | 3/20 | 15.0% | +5.43% | **+0.82%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.50% | **+0.40%** |
| ASK | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.24% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.02% | **+0.26%** |
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.46% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$225.97** / 初期 $100.00 (+125.97%)
- 確定: 1969件 (Win 571 / Loss 640 / Flat 758) / skip 1785件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $225.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 294件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T01:48:28.244264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=63550.0
- Funnel: target 795 → liquid 147 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1, 4h RSI 78.6 >= 65=1, 4h RSI 82.6 >= 65=1, 4h RSI 75.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BICO/USDT:USDT | +36.43% | $16,401,271.44 |
| BLESS/USDT:USDT | +26.67% | $5,214,410.00 |
| BTW/USDT:USDT | +22.83% | $13,776,079.96 |
| RE/USDT:USDT | +22.67% | $79,055,110.32 |
| EIGEN/USDT:USDT | +18.49% | $5,660,006.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APE/USDT:USDT | below_1h_threshold | +3.01% | +2.93% |
| PI/USDT:USDT | below_1h_threshold | +2.07% | +1.98% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.63% | +1.55% |
| HIGH/USDT:USDT | below_1h_threshold | +1.52% | +1.43% |
| RENDER/USDT:USDT | below_1h_threshold | +1.45% | +1.36% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
