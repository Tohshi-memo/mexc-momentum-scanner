# Decision Report

- generated_at: 2026-05-23T00:53:59.694796+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4746**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.84% / filled 20/20。**
- 全期間 MARKET基準: n=4746, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.84%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.53% | **+1.53%** |
| MARKET | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.64% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.81% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$96.20** / 初期 $100.00 (-3.80%)
- 確定トレード: 61件 (TP 16 / SL 42 / EXP 3)
- 最新: PLAY/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.20
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.81** / 初期 $100.00 (+23.81%)
- 確定: 592件 (Win 149 / Loss 190 / Flat 253) / skip 715件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $123.81

## 4. Latest Market Context

- 更新: 2026-05-23T00:53:54.911161+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=75370.0
- Funnel: target 764 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +95.22% | $48,317,937.08 |
| BEAT/USDT:USDT | +16.79% | $50,429,715.20 |
| BILL/USDT:USDT | +15.34% | $17,244,756.97 |
| TAG/USDT:USDT | +13.73% | $1,209,105.54 |
| GUA/USDT:USDT | +6.34% | $1,352,021.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEX/USDT:USDT | below_1h_threshold | +3.75% | +3.93% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.63% | +2.81% |
| GUA/USDT:USDT | below_1h_threshold | +2.03% | +2.22% |
| TAG/USDT:USDT | below_1h_threshold | +1.98% | +2.16% |
| SIREN/USDT:USDT | below_1h_threshold | +1.55% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
