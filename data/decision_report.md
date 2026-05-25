# Decision Report

- generated_at: 2026-05-25T22:44:18.379473+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4873**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.99% / filled 20/20。**
- 全期間 MARKET基準: n=4873, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.48% | **+2.48%** |
| MARKET | 20/20 | 100.0% | +1.99% | **+1.99%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.92% | **+1.63%** |
| LIMIT_BB3S | 6/12 | 50.0% | +0.77% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.49% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.13% | **+0.11%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +0.09% | **+0.08%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 761件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T22:44:16.291418+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=77135.7
- Funnel: target 765 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +68.57% | $1,630,107.59 |
| GRASS/USDT:USDT | +14.76% | $7,099,898.65 |
| WLD/USDT:USDT | +7.80% | $45,155,569.04 |
| ERA/USDT:USDT | +6.21% | $1,831,866.44 |
| NIL/USDT:USDT | +5.80% | $15,526,070.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +2.30% | +2.56% |
| NIL/USDT:USDT | below_1h_threshold | +2.20% | +2.46% |
| LAB/USDT:USDT | below_1h_threshold | +1.68% | +1.95% |
| H/USDT:USDT | below_1h_threshold | +1.02% | +1.28% |
| GUA/USDT:USDT | below_1h_threshold | +0.94% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
