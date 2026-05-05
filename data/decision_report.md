# Decision Report

- generated_at: 2026-05-05T01:07:25.411349+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3284**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.83% / filled 20/20。**
- 全期間 MARKET基準: n=3284, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.42% | **+2.17%** |
| MARKET | 20/20 | 100.0% | +1.83% | **+1.83%** |
| ASK | 20/20 | 100.0% | +1.78% | **+1.78%** |
| LIMIT_BB3S | 2/12 | 16.7% | +4.73% | **+0.79%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +5.24% | **+1.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.91% | **+0.49%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.58% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T01:07:23.533914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=80129.9
- Funnel: target 761 → liquid 201 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +26.50% | $59,710,258.19 |
| TONCOIN/USDT:USDT | +24.93% | $48,111,262.22 |
| FHE/USDT:USDT | +20.53% | $2,635,961.87 |
| NOT/USDT:USDT | +14.49% | $1,021,594.75 |
| PLAY/USDT:USDT | +13.24% | $2,685,181.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +4.13% | +4.13% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.06% | +2.07% |
| WLFI/USDT:USDT | below_1h_threshold | +1.42% | +1.42% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.37% | +1.37% |
| TIA/USDT:USDT | below_1h_threshold | +1.33% | +1.33% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
