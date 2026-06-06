# Decision Report

- generated_at: 2026-06-06T04:15:38.823011+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5781**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.86% / filled 20/20。**
- 全期間 MARKET基準: n=5781, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.95% | **+1.95%** |
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.14% | **+0.66%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +0.67% | **+0.54%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.22% | **+0.42%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.50% | **+0.30%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1330件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T04:15:35.615254+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.08% price=60006.5
- Funnel: target 771 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +32.29% | $5,330,403.56 |
| VELVET/USDT:USDT | +25.84% | $2,018,501.42 |
| OPN/USDT:USDT | +16.51% | $22,984,624.69 |
| CLO/USDT:USDT | +15.80% | $1,690,103.27 |
| ALLO/USDT:USDT | +15.37% | $8,182,693.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +1.89% | +2.97% |
| VELVET/USDT:USDT | below_1h_threshold | +1.03% | +2.11% |
| HEI/USDT:USDT | below_1h_threshold | +0.22% | +1.30% |
| EPIC/USDT:USDT | below_1h_threshold | +0.10% | +1.18% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.01% | +1.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
