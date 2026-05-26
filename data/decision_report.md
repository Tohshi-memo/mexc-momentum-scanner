# Decision Report

- generated_at: 2026-05-26T00:29:19.065538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4877**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.25% / filled 20/20。**
- 全期間 MARKET基準: n=4877, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.73% | **+2.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.61% | **+2.34%** |
| MARKET | 20/20 | 100.0% | +2.25% | **+2.25%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.02% | **+0.56%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | -0.23% | **-0.19%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 765件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-26T00:29:16.293801+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=77125.5
- Funnel: target 765 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +78.57% | $1,751,964.68 |
| GRASS/USDT:USDT | +16.79% | $7,750,774.39 |
| ERA/USDT:USDT | +10.58% | $1,941,090.96 |
| WLD/USDT:USDT | +8.66% | $46,799,822.04 |
| NIL/USDT:USDT | +7.46% | $15,372,584.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +4.89% | +5.09% |
| NIL/USDT:USDT | below_1h_threshold | +2.98% | +3.18% |
| AGT/USDT:USDT | below_1h_threshold | +2.87% | +3.07% |
| GRASS/USDT:USDT | below_1h_threshold | +1.47% | +1.67% |
| PHA/USDT:USDT | below_1h_threshold | +1.08% | +1.29% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
