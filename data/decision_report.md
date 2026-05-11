# Decision Report

- generated_at: 2026-05-11T01:08:11.256830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4001**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=4001, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| ASK | 20/20 | 100.0% | +1.69% | **+1.69%** |
| LIMIT_BB3S | 6/13 | 46.2% | +2.96% | **+1.37%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.48% | **+1.26%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.56% | **+0.91%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.69% | **+1.27%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.88% | **+0.75%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.67% | **+0.57%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.70% | **+0.42%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.93** / 初期 $100.00 (+8.93%)
- 確定: 208件 (Win 52 / Loss 71 / Flat 85) / skip 354件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNDKSTOCK/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $108.93

## 4. Latest Market Context

- 更新: 2026-05-11T01:08:08.156710+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=81394.8
- Funnel: target 771 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +42.92% | $8,884,194.28 |
| ALCH/USDT:USDT | +20.06% | $3,781,223.83 |
| TROLLSOL/USDT:USDT | +16.41% | $5,290,242.83 |
| B/USDT:USDT | +11.99% | $2,535,737.34 |
| OG/USDT:USDT | +9.23% | $1,498,223.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +2.24% | +2.28% |
| PLAY/USDT:USDT | below_1h_threshold | +1.92% | +1.96% |
| TRUTH/USDT:USDT | below_1h_threshold | +1.28% | +1.32% |
| ALCH/USDT:USDT | below_1h_threshold | +1.24% | +1.29% |
| ONDO/USDT:USDT | below_1h_threshold | +0.92% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
