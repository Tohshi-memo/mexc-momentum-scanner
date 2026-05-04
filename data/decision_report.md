# Decision Report

- generated_at: 2026-05-04T03:42:23.620975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3137**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3137, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.64% | **-0.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_BB3S | 5/16 | 31.2% | +0.50% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.32% | **+1.74%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.28% | **+1.15%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.35% | **+0.67%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.07% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T03:42:19.560004+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=79896.2
- Funnel: target 757 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +50.55% | $234,503,998.26 |
| SKYAI/USDT:USDT | +43.95% | $37,322,431.97 |
| TAG/USDT:USDT | +38.67% | $6,177,921.01 |
| BSB/USDT:USDT | +31.61% | $15,699,068.22 |
| GIGA/USDT:USDT | +28.56% | $1,124,675.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.22% | +4.51% |
| DASH/USDT:USDT | below_1h_threshold | +3.81% | +4.11% |
| AIOT/USDT:USDT | below_1h_threshold | +2.27% | +2.56% |
| SIREN/USDT:USDT | below_1h_threshold | +2.05% | +2.34% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.65% | +1.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
