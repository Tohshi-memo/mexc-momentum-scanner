# Decision Report

- generated_at: 2026-05-04T01:37:05.939058+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3124**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3124, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 5/19 | 26.3% | +1.66% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.47% | **+1.74%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.24%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.53% | **+1.07%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T01:37:03.743250+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=78806.4
- Funnel: target 757 → liquid 166 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +68.39% | $246,080,083.22 |
| SKYAI/USDT:USDT | +56.69% | $33,232,151.44 |
| TAG/USDT:USDT | +27.47% | $3,891,657.27 |
| GIGA/USDT:USDT | +22.38% | $1,091,785.35 |
| BSB/USDT:USDT | +16.64% | $15,272,898.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +3.74% | +3.36% |
| B/USDT:USDT | below_1h_threshold | +3.20% | +2.82% |
| ORDI/USDT:USDT | below_1h_threshold | +2.37% | +1.99% |
| DOGE/USDT:USDT | below_1h_threshold | +2.35% | +1.97% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.23% | +1.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
