# Decision Report

- generated_at: 2026-06-02T17:38:23.708143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5475**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5475, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.90% | **-0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +6.21% | **+0.93%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +7.48% | **+7.48%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.39% | **+1.05%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.93% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 89件 (TP 26 / SL 60 / EXP 3)
- 最新: ENA/USDT:USDT SL_HIT PnL -3.88% 残高後 $97.10
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1060件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T17:38:18.199878+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=67629.1
- Funnel: target 770 → liquid 153 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +51.21% | $10,534,357.64 |
| LIT/USDT:USDT | +15.88% | $3,068,849.71 |
| ENA/USDT:USDT | +15.41% | $35,722,212.37 |
| PIEVERSE/USDT:USDT | +10.96% | $5,538,299.90 |
| VVV/USDT:USDT | +8.41% | $7,148,911.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.28% | +3.93% |
| NEAR/USDT:USDT | below_1h_threshold | +3.80% | +3.45% |
| APE/USDT:USDT | below_1h_threshold | +3.49% | +3.14% |
| PENDLE/USDT:USDT | below_1h_threshold | +2.97% | +2.62% |
| OP/USDT:USDT | below_1h_threshold | +2.94% | +2.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
