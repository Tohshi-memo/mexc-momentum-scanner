# Decision Report

- generated_at: 2026-05-02T08:32:00.197060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2881**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=2881, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT | 20/20 | 100.0% | +1.01% | **+1.01%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.49% | **+1.26%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.97% | **+0.40%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.38% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T08:31:58.259193+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78249.6
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +183.00% | $86,655,408.73 |
| KNC/USDT:USDT | +24.47% | $1,523,284.01 |
| IRYS/USDT:USDT | +17.11% | $1,365,320.47 |
| BIO/USDT:USDT | +13.75% | $1,374,399.05 |
| BLESS/USDT:USDT | +13.05% | $2,228,838.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +4.28% | +4.20% |
| MOVR/USDT:USDT | below_1h_threshold | +3.58% | +3.49% |
| RLS/USDT:USDT | below_1h_threshold | +2.85% | +2.76% |
| BSB/USDT:USDT | below_1h_threshold | +2.77% | +2.68% |
| TAC/USDT:USDT | below_1h_threshold | +2.67% | +2.58% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
