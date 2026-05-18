# Decision Report

- generated_at: 2026-05-18T05:13:30.025474+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4434**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=4434, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.51% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.28%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.78% | **+0.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.86** / 初期 $100.00 (+19.86%)
- 確定: 431件 (Win 111 / Loss 147 / Flat 173) / skip 564件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.86

## 4. Latest Market Context

- 更新: 2026-05-18T05:13:27.500168+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77026.7
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +31.75% | $6,092,449.35 |
| BSB/USDT:USDT | +10.46% | $19,206,625.32 |
| OPENLEDGER/USDT:USDT | +6.43% | $1,261,805.62 |
| AKT/USDT:USDT | +6.39% | $1,493,489.88 |
| ZEC/USDT:USDT | +5.59% | $482,038,154.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +3.92% | +3.89% |
| PLAY/USDT:USDT | below_1h_threshold | +2.07% | +2.04% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.62% | +1.58% |
| SPACE/USDT:USDT | below_1h_threshold | +0.67% | +0.64% |
| OPENLEDGER/USDT:USDT | below_1h_threshold | +0.67% | +0.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
