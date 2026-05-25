# Decision Report

- generated_at: 2026-05-25T23:24:22.258423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4874**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=4874, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.75% | **+2.75%** |
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.30% | **+1.96%** |
| LIMIT_BB3S | 5/11 | 45.5% | +1.36% | **+0.62%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.49% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.13% | **+0.11%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.02% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 762件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T23:24:20.150536+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=77252.6
- Funnel: target 765 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +71.42% | $1,650,279.93 |
| GRASS/USDT:USDT | +15.14% | $7,423,840.52 |
| WLD/USDT:USDT | +8.96% | $44,537,598.31 |
| ERA/USDT:USDT | +5.78% | $1,839,339.21 |
| TIA/USDT:USDT | +5.40% | $20,409,127.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +1.94% | +1.72% |
| TIA/USDT:USDT | below_1h_threshold | +1.84% | +1.62% |
| WLD/USDT:USDT | below_1h_threshold | +1.47% | +1.26% |
| FET/USDT:USDT | below_1h_threshold | +1.10% | +0.88% |
| INJ/USDT:USDT | below_1h_threshold | +0.76% | +0.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
