# Decision Report

- generated_at: 2026-07-04T02:35:38.620911+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8213**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8213, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.05% | **-1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.43% | **+1.14%** |
| ASK_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.28% | **+0.71%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$299.08** / 初期 $100.00 (+199.08%)
- 確定: 2531件 (Win 783 / Loss 844 / Flat 904) / skip 2243件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $299.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.83** / 初期 $100.00 (+5.83%)
- 確定: 612件 (Win 147 / Loss 148 / Flat 317) / skip 1012件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.20% 残高後 $105.83

## 5. Latest Market Context

- 更新: 2026-07-04T02:35:32.350661+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=62411.8
- Funnel: target 834 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +81.54% | $3,697,380.75 |
| MAGMA/USDT:USDT | +35.79% | $14,524,024.43 |
| TLM/USDT:USDT | +34.66% | $38,909,613.15 |
| BAS/USDT:USDT | +26.77% | $4,118,085.01 |
| HMSTR/USDT:USDT | +26.36% | $1,981,480.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRB/USDT:USDT | below_1h_threshold | +4.73% | +4.79% |
| HMSTR/USDT:USDT | below_1h_threshold | +4.73% | +4.79% |
| VELVET/USDT:USDT | below_1h_threshold | +2.80% | +2.86% |
| TAIKO/USDT:USDT | below_1h_threshold | +2.35% | +2.41% |
| LIT/USDT:USDT | below_1h_threshold | +2.31% | +2.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
