# Decision Report

- generated_at: 2026-05-08T10:17:41.503005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3769**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.14% / filled 20/20。**
- 全期間 MARKET基準: n=3769, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+3.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.14% | **+3.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.14% | **+3.14%** |
| ASK | 20/20 | 100.0% | +3.04% | **+3.04%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.59% | **+2.20%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.03% | **+0.62%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.52% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +1.19% | **+0.68%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.03% | **-0.21%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | -0.32% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 139件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T10:17:38.260176+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=79793.6
- Funnel: target 773 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +40.69% | $6,349,627.72 |
| PLAY/USDT:USDT | +38.69% | $8,759,600.17 |
| BSB/USDT:USDT | +37.78% | $8,758,907.74 |
| STRK/USDT:USDT | +28.59% | $17,233,806.49 |
| AGT/USDT:USDT | +22.93% | $5,448,846.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHAROS/USDT:USDT | below_1h_threshold | +2.20% | +2.24% |
| CHIP/USDT:USDT | below_1h_threshold | +1.97% | +2.01% |
| PLAY/USDT:USDT | below_1h_threshold | +1.78% | +1.82% |
| ONDO/USDT:USDT | below_1h_threshold | +1.55% | +1.59% |
| SATO/USDT:USDT | below_1h_threshold | +1.37% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
