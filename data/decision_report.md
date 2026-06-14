# Decision Report

- generated_at: 2026-06-14T14:40:02.917063+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6671**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.08% / filled 20/20。**
- 全期間 MARKET基準: n=6671, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.62% | **+0.49%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.59% | **+0.27%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.05% | **+0.42%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.80** / 初期 $100.00 (+73.80%)
- 確定: 1544件 (Win 411 / Loss 488 / Flat 645) / skip 1688件
- 成長率目線: 平均log +0.000358 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $173.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定: 58件 (Win 19 / Loss 12 / Flat 27) / skip 24件
- 成長率目線: 平均log -0.000173 / 幾何平均 -0.017% per trade / maxDD +2.00%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0071 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $99.00

## 5. Latest Market Context

- 更新: 2026-06-14T14:39:58.442599+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.59% price=63906.3
- Funnel: target 770 → liquid 129 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +33.90% | $91,387,118.43 |
| ZKC/USDT:USDT | +32.22% | $1,566,439.05 |
| CLO/USDT:USDT | +29.78% | $1,096,388.08 |
| TRADOOR/USDT:USDT | +28.41% | $8,762,447.87 |
| OPG/USDT:USDT | +21.26% | $1,699,655.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +3.19% | +3.78% |
| RIF/USDT:USDT | below_1h_threshold | +2.82% | +3.41% |
| BSB/USDT:USDT | below_1h_threshold | +1.96% | +2.55% |
| LAB/USDT:USDT | below_1h_threshold | +1.13% | +1.71% |
| CLO/USDT:USDT | below_1h_threshold | +0.88% | +1.47% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
