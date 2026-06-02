# Decision Report

- generated_at: 2026-06-02T21:07:16.662369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5489**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5489, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.23% | **-2.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.16% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.96% | **+2.96%** |
| MARKET_LONG | 20/20 | 100.0% | +2.78% | **+2.78%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.50% | **+2.45%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.77% | **+2.07%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.19% | **+1.57%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1074件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T21:07:14.306870+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=67696.2
- Funnel: target 769 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +31.96% | $12,331,046.27 |
| LAB/USDT:USDT | +23.59% | $191,090,514.13 |
| ESPORTS/USDT:USDT | +15.95% | $8,933,071.05 |
| LIT/USDT:USDT | +14.95% | $5,731,824.69 |
| ENA/USDT:USDT | +12.08% | $45,878,518.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +1.93% | +1.72% |
| NEAR/USDT:USDT | below_1h_threshold | +1.11% | +0.90% |
| RENDER/USDT:USDT | below_1h_threshold | +0.96% | +0.75% |
| ENA/USDT:USDT | below_1h_threshold | +0.94% | +0.74% |
| VVV/USDT:USDT | below_1h_threshold | +0.90% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
