# Decision Report

- generated_at: 2026-05-20T11:58:44.910809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4541**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.93% / filled 20/20。**
- 全期間 MARKET基準: n=4541, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.95% | **+0.95%** |
| MARKET | 20/20 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.39% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.20% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.39** / 初期 $100.00 (+24.39%)
- 確定: 503件 (Win 131 / Loss 173 / Flat 199) / skip 599件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $124.39

## 4. Latest Market Context

- 更新: 2026-05-20T11:58:42.833663+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=77349.9
- Funnel: target 763 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +94.31% | $2,136,239.74 |
| FIDA/USDT:USDT | +34.42% | $3,112,946.70 |
| PLAY/USDT:USDT | +27.54% | $10,288,067.66 |
| PROMPT/USDT:USDT | +27.48% | $12,718,443.28 |
| EDEN/USDT:USDT | +26.67% | $22,754,172.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.77% | +4.93% |
| SATO/USDT:USDT | below_1h_threshold | +3.91% | +4.07% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.80% | +2.96% |
| CHIP/USDT:USDT | below_1h_threshold | +2.57% | +2.73% |
| HOME/USDT:USDT | below_1h_threshold | +2.34% | +2.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
