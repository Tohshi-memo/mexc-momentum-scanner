# Decision Report

- generated_at: 2026-06-07T23:26:04.609343+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6009**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6009, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.89% | **+0.27%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |
| MARKET | 20/20 | 100.0% | -0.33% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.55% | **+1.55%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.96% | **+0.82%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.99% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$153.10** / 初期 $100.00 (+53.10%)
- 確定: 1126件 (Win 275 / Loss 341 / Flat 510) / skip 1444件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $153.10

## 4. Latest Market Context

- 更新: 2026-06-07T23:26:01.347093+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=63026.3
- Funnel: target 769 → liquid 134 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +27.25% | $4,099,482.29 |
| BTW/USDT:USDT | +23.23% | $15,549,560.75 |
| PIPPIN/USDT:USDT | +20.95% | $4,798,807.77 |
| BEAT/USDT:USDT | +18.05% | $80,561,855.13 |
| BLESS/USDT:USDT | +17.69% | $8,553,800.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.34% | +4.04% |
| BABY/USDT:USDT | below_1h_threshold | +2.15% | +1.84% |
| BLESS/USDT:USDT | below_1h_threshold | +1.90% | +1.60% |
| MYX/USDT:USDT | below_1h_threshold | +1.29% | +0.99% |
| KAS/USDT:USDT | below_1h_threshold | +1.24% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
