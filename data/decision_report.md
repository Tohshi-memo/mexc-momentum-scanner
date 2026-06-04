# Decision Report

- generated_at: 2026-06-04T01:23:39.853624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5589**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.91% / filled 20/20。**
- 全期間 MARKET基準: n=5589, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+2.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.91% | **+2.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.93% | **+2.93%** |
| MARKET | 20/20 | 100.0% | +2.91% | **+2.91%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.97% | **+2.68%** |
| LIMIT_2PCT | 13/20 | 65.0% | +2.32% | **+1.51%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.49% | **+1.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.25% | **+0.67%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +0.69% | **+0.27%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.21% | **+0.13%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.10% | **-0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.06** / 初期 $100.00 (-1.94%)
- 確定トレード: 93件 (TP 28 / SL 62 / EXP 3)
- 最新: XPL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.06
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1145件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T01:23:37.505184+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.16% price=62578.2
- Funnel: target 769 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPN/USDT:USDT | +28.51% | $22,435,096.83 |
| STO/USDT:USDT | +18.45% | $6,686,281.23 |
| MAGMA/USDT:USDT | +8.13% | $4,328,106.63 |
| EPIC/USDT:USDT | +6.56% | $3,540,553.08 |
| BP/USDT:USDT | +5.29% | $1,560,507.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OPN/USDT:USDT | below_1h_threshold | +2.37% | +3.52% |
| GUA/USDT:USDT | below_1h_threshold | +1.39% | +2.55% |
| ZORA/USDT:USDT | below_1h_threshold | +0.87% | +2.03% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.82% | +1.98% |
| BEAT/USDT:USDT | below_1h_threshold | +0.68% | +1.84% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
