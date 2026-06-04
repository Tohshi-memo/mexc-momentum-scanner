# Decision Report

- generated_at: 2026-06-04T10:34:05.695457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5620**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.80% / filled 20/20。**
- 全期間 MARKET基準: n=5620, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +4.34% | **+4.34%** |
| MARKET | 20/20 | 100.0% | +3.80% | **+3.80%** |
| LIMIT_1PCT | 14/20 | 70.0% | +3.00% | **+2.10%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.20% | **+1.21%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.19% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +0.22% | **+0.15%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.65% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1006件 (Win 239 / Loss 312 / Flat 455) / skip 1175件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T10:34:00.165796+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -1.03% price=62585.1
- Funnel: target 771 → liquid 173 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +28.89% | $6,036,808.50 |
| OPN/USDT:USDT | +26.74% | $33,720,348.27 |
| HEI/USDT:USDT | +25.67% | $4,445,922.57 |
| SIREN/USDT:USDT | +22.95% | $4,959,329.45 |
| LAB/USDT:USDT | +13.48% | $133,179,828.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.07% | +5.10% |
| PLAY/USDT:USDT | below_1h_threshold | +2.49% | +3.52% |
| BP/USDT:USDT | below_1h_threshold | +1.71% | +2.74% |
| EPIC/USDT:USDT | below_1h_threshold | +1.14% | +2.17% |
| MEME/USDT:USDT | below_1h_threshold | +1.03% | +2.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
