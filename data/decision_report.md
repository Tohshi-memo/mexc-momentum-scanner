# Decision Report

- generated_at: 2026-06-02T22:07:09.957446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5494**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5494, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.56% | **+0.89%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.21% | **+0.54%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.41% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.09% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/8 | 75.0% | +3.10% | **+2.32%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.18% | **+1.74%** |
| ASK_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.58% | **+1.58%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.34% | **+1.52%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1079件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T22:07:07.547362+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=67380.5
- Funnel: target 769 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +29.43% | $12,541,575.39 |
| BBSTOCK/USDT:USDT | +18.33% | $1,642,814.65 |
| US/USDT:USDT | +16.44% | $6,431,000.27 |
| LIT/USDT:USDT | +16.04% | $6,409,400.89 |
| GENIUS/USDT:USDT | +14.26% | $1,024,350.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PANWSTOCK/USDT:USDT | below_1h_threshold | +2.17% | +2.39% |
| US/USDT:USDT | below_1h_threshold | +2.11% | +2.33% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.91% | +2.14% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.79% |
| BBSTOCK/USDT:USDT | below_1h_threshold | +1.57% | +1.79% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
