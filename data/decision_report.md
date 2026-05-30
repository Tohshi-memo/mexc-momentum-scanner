# Decision Report

- generated_at: 2026-05-30T10:20:04.984404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5116**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=5116, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.09% | **+1.09%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.12% | **+0.84%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.62% | **+0.55%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.59% | **+0.44%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.12** / 初期 $100.00 (+27.12%)
- 確定: 771件 (Win 181 / Loss 232 / Flat 358) / skip 906件
- 成長率目線: 平均log +0.000311 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NFP/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $127.12

## 4. Latest Market Context

- 更新: 2026-05-30T10:20:02.539843+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=73620.9
- Funnel: target 773 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NFP/USDT:USDT | +55.60% | $2,417,980.05 |
| HEI/USDT:USDT | +35.49% | $17,341,863.50 |
| LAB/USDT:USDT | +24.71% | $126,780,922.83 |
| VTHO/USDT:USDT | +23.57% | $1,448,460.29 |
| H/USDT:USDT | +18.90% | $1,686,106.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.12% | +2.06% |
| BASED/USDT:USDT | below_1h_threshold | +1.95% | +1.89% |
| GRASS/USDT:USDT | below_1h_threshold | +1.36% | +1.30% |
| HEI/USDT:USDT | below_1h_threshold | +1.04% | +0.98% |
| VVV/USDT:USDT | below_1h_threshold | +1.00% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
