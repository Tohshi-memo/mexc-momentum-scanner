# Decision Report

- generated_at: 2026-05-26T06:04:31.165394+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4887**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.92% / filled 20/20。**
- 全期間 MARKET基準: n=4887, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.92% | **+1.92%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.96% | **+1.86%** |
| ASK | 20/20 | 100.0% | +1.86% | **+1.86%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.14% | **+0.63%** |
| LIMIT_3PCT | 10/20 | 50.0% | +0.82% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.67% | **+0.73%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.23% | **+0.25%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.16% | **+0.08%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 775件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-26T06:04:29.011447+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=76819.7
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +78.57% | $2,408,557.47 |
| WLD/USDT:USDT | +12.88% | $61,786,281.87 |
| GRASS/USDT:USDT | +10.88% | $8,990,359.97 |
| AKT/USDT:USDT | +5.20% | $1,489,111.26 |
| FET/USDT:USDT | +4.88% | $15,633,939.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| POND/USDT:USDT | below_1h_threshold | +1.63% | +1.71% |
| RENDER/USDT:USDT | below_1h_threshold | +0.48% | +0.57% |
| ERA/USDT:USDT | below_1h_threshold | +0.21% | +0.30% |
| LAB/USDT:USDT | below_1h_threshold | +0.18% | +0.27% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.10% | +0.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
