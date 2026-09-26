# Decision Report

- generated_at: 2026-09-26T06:56:36.099300+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15580**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15580, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.94% | **-1.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.30% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.21% | **+2.57%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.54% | **+2.41%** |
| MARKET_LONG | 20/20 | 100.0% | +1.94% | **+1.94%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.56% | **+0.70%** |

## 2. $100 Live Portfolio

- 残高: **$120.79** / 初期 $100.00 (+20.79%)
- 確定トレード: 223件 (TP 82 / SL 135 / EXP 6)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.79
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.44** / 初期 $100.00 (+1165.44%)
- 確定: 5941件 (Win 1755 / Loss 1904 / Flat 2282) / skip 6200件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,265.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$264.93** / 初期 $100.00 (+164.93%)
- 確定: 3510件 (Win 967 / Loss 800 / Flat 1743) / skip 5481件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1234 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PAID/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $264.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.41** / 初期 $100.00 (+19.41%)
- 確定: 3185件 (Win 937 / Loss 1262 / Flat 986) / pending 1件 / skip 3865件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000474 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LDO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.03% 残高後 $119.41

## 6. Latest Market Context

- 更新: 2026-09-26T06:56:20.026557+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=83879.5
- Funnel: target 1067 → liquid 162 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1, 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PAID/USDT:USDT | +353.97% | $1,349,507.35 |
| BATON/USDT:USDT | +32.94% | $1,578,281.72 |
| RARE/USDT:USDT | +27.68% | $2,194,076.01 |
| ARK/USDT:USDT | +24.12% | $3,790,844.15 |
| AERO/USDT:USDT | +13.66% | $4,637,709.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CC/USDT:USDT | below_1h_threshold | +3.29% | +3.31% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.95% | +2.96% |
| FILECOIN/USDT:USDT | below_1h_threshold | +2.68% | +2.70% |
| BR/USDT:USDT | below_1h_threshold | +2.50% | +2.51% |
| ATOM/USDT:USDT | below_1h_threshold | +1.83% | +1.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
