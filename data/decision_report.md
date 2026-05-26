# Decision Report

- generated_at: 2026-05-26T02:30:00.402898+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4881**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.88% / filled 20/20。**
- 全期間 MARKET基準: n=4881, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.88% | **+2.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.41% | **+3.41%** |
| LIMIT_1PCT | 18/20 | 90.0% | +3.21% | **+2.89%** |
| MARKET | 20/20 | 100.0% | +2.88% | **+2.88%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.98% | **+0.54%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | -0.05% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 769件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-26T02:29:55.158491+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=76641.3
- Funnel: target 768 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +82.14% | $1,906,853.35 |
| GRASS/USDT:USDT | +12.51% | $8,212,564.62 |
| WLD/USDT:USDT | +8.76% | $49,616,671.62 |
| AKT/USDT:USDT | +4.22% | $1,395,337.64 |
| ERA/USDT:USDT | +3.17% | $2,021,176.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.80% | +2.90% |
| H/USDT:USDT | below_1h_threshold | +2.20% | +2.29% |
| LUNC/USDT:USDT | below_1h_threshold | +1.31% | +1.41% |
| POND/USDT:USDT | below_1h_threshold | +1.19% | +1.29% |
| AKT/USDT:USDT | below_1h_threshold | +0.86% | +0.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
