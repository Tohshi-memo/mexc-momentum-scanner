# Decision Report

- generated_at: 2026-05-11T02:07:44.699476+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4002**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.15% / filled 20/20。**
- 全期間 MARKET基準: n=4002, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/13 | 46.2% | +2.96% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.15% | **+1.15%** |
| ASK | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.25% | **+1.13%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.35% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.09% | **+1.47%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.41% | **+1.19%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.30% | **+1.11%** |
| LIMIT_BB3S_LONG | 7/7 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.06% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.66** / 初期 $100.00 (+9.66%)
- 確定: 209件 (Win 53 / Loss 71 / Flat 85) / skip 354件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.67% 残高後 $109.66

## 4. Latest Market Context

- 更新: 2026-05-11T02:07:41.790297+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=81364.1
- Funnel: target 775 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +33.25% | $9,572,951.05 |
| TROLLSOL/USDT:USDT | +22.42% | $5,333,375.66 |
| ALCH/USDT:USDT | +22.06% | $3,861,370.76 |
| B/USDT:USDT | +12.77% | $2,650,662.95 |
| OPG/USDT:USDT | +10.07% | $1,073,152.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +0.89% | +1.02% |
| JASMY/USDT:USDT | below_1h_threshold | +0.62% | +0.74% |
| SAHARA/USDT:USDT | below_1h_threshold | +0.58% | +0.70% |
| NIL/USDT:USDT | below_1h_threshold | +0.49% | +0.61% |
| ALCH/USDT:USDT | below_1h_threshold | +0.24% | +0.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
