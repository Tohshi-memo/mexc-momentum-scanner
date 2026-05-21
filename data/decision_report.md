# Decision Report

- generated_at: 2026-05-21T11:18:54.274601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4619**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4619, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.65% | **+1.41%** |
| ASK | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.03% | **+0.75%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.01% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.06% | **+0.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.21% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 634件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T11:18:52.258710+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=77299.5
- Funnel: target 766 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +51.18% | $4,090,023.45 |
| EDEN/USDT:USDT | +38.94% | $30,577,427.00 |
| ROAM/USDT:USDT | +35.87% | $2,230,819.88 |
| MITO/USDT:USDT | +35.67% | $1,081,619.40 |
| USELESS/USDT:USDT | +18.43% | $2,016,011.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.13% | +1.96% |
| LIT/USDT:USDT | below_1h_threshold | +1.88% | +1.72% |
| MONAD/USDT:USDT | below_1h_threshold | +1.27% | +1.10% |
| NIL/USDT:USDT | below_1h_threshold | +1.20% | +1.03% |
| RIVER/USDT:USDT | below_1h_threshold | +0.74% | +0.58% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
