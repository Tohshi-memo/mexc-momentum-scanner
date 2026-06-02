# Decision Report

- generated_at: 2026-06-02T17:16:06.045842+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5471**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5471, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.32% | **-0.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.65% | **+0.62%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.32% | **+0.53%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.36% | **+1.53%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.85% | **+1.02%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.83% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$97.10** / 初期 $100.00 (-2.90%)
- 確定トレード: 89件 (TP 26 / SL 60 / EXP 3)
- 最新: ENA/USDT:USDT SL_HIT PnL -3.88% 残高後 $97.10
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1056件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T17:16:00.610881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=67449.9
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +23.20% | $9,416,879.68 |
| ENA/USDT:USDT | +12.76% | $33,986,704.77 |
| LIT/USDT:USDT | +12.43% | $2,719,421.81 |
| PIEVERSE/USDT:USDT | +9.23% | $5,343,853.69 |
| SKYAI/USDT:USDT | +8.38% | $30,699,114.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.96% | +3.87% |
| ONDO/USDT:USDT | below_1h_threshold | +3.77% | +3.68% |
| ENA/USDT:USDT | below_1h_threshold | +3.26% | +3.17% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.78% | +2.69% |
| ICP/USDT:USDT | below_1h_threshold | +2.56% | +2.47% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
