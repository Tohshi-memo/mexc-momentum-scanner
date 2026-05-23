# Decision Report

- generated_at: 2026-05-23T01:04:00.586439+00:00
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

- 更新: 2026-05-23T01:03:58.463347+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=75444.6
- Funnel: target 764 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +103.03% | $48,415,961.06 |
| BEAT/USDT:USDT | +19.54% | $50,753,325.38 |
| BILL/USDT:USDT | +16.46% | $17,106,019.52 |
| TAG/USDT:USDT | +13.52% | $1,232,721.89 |
| NEX/USDT:USDT | +10.75% | $1,237,063.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEX/USDT:USDT | below_1h_threshold | +2.54% | +2.39% |
| ATOM/USDT:USDT | below_1h_threshold | +0.67% | +0.52% |
| SAGA/USDT:USDT | below_1h_threshold | +0.55% | +0.40% |
| BEAT/USDT:USDT | below_1h_threshold | +0.54% | +0.38% |
| NIL/USDT:USDT | below_1h_threshold | +0.52% | +0.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
