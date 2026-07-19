# Decision Report

- generated_at: 2026-07-19T09:06:17.357393+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9016**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9016, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.96% | **-2.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 4/17 | 23.5% | +1.54% | **+0.36%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.98% | **+0.25%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.28% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +4.15% | **+3.11%** |
| MARKET_LONG | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| LIMIT_2PCT_LONG | 7/20 | 35.0% | +3.85% | **+1.35%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +4.31% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$401.29** / 初期 $100.00 (+301.29%)
- 確定: 3078件 (Win 964 / Loss 977 / Flat 1137) / skip 2499件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $401.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.54** / 初期 $100.00 (+27.54%)
- 確定: 977件 (Win 250 / Loss 197 / Flat 530) / skip 1450件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2384 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $127.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.68** / 初期 $100.00 (+0.68%)
- 確定: 219件 (Win 70 / Loss 109 / Flat 40) / pending 6件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000527 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.68

## 6. Latest Market Context

- 更新: 2026-07-19T09:06:10.731277+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64669.1
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +125.34% | $44,119,616.14 |
| BANK/USDT:USDT | +68.93% | $19,759,260.58 |
| TLM/USDT:USDT | +50.37% | $5,613,141.14 |
| B/USDT:USDT | +36.53% | $40,782,361.04 |
| BULLA/USDT:USDT | +25.53% | $1,307,318.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.84% | +2.85% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.63% | +1.64% |
| AKE/USDT:USDT | below_1h_threshold | +1.23% | +1.24% |
| BULLA/USDT:USDT | below_1h_threshold | +1.20% | +1.21% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.09% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
