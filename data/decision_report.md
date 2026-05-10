# Decision Report

- generated_at: 2026-05-10T23:27:51.391281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3997**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.30% / filled 20/20。**
- 全期間 MARKET基準: n=3997, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.30% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.21%** |
| LIMIT_BB3S | 7/13 | 53.8% | +2.04% | **+1.10%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.67% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.54% | **+1.31%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.31% | **+0.26%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.37% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.94** / 初期 $100.00 (+8.94%)
- 確定: 205件 (Win 51 / Loss 69 / Flat 85) / skip 353件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $108.94

## 4. Latest Market Context

- 更新: 2026-05-10T23:27:48.485879+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=82300.0
- Funnel: target 770 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +49.36% | $7,565,182.90 |
| TROLLSOL/USDT:USDT | +22.33% | $4,886,364.26 |
| ALCH/USDT:USDT | +22.06% | $3,552,601.88 |
| B/USDT:USDT | +13.97% | $2,391,973.89 |
| DEEP/USDT:USDT | +10.56% | $2,406,388.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEEP/USDT:USDT | below_1h_threshold | +1.80% | +1.45% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.43% | +1.08% |
| BAS/USDT:USDT | below_1h_threshold | +1.27% | +0.91% |
| CRO/USDT:USDT | below_1h_threshold | +1.20% | +0.84% |
| SPX/USDT:USDT | below_1h_threshold | +0.99% | +0.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
