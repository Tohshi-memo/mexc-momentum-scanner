# Decision Report

- generated_at: 2026-07-02T14:43:51.150064+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8089**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8089, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.22% | **+0.52%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_7PCT | 5/20 | 25.0% | +0.08% | **+0.02%** |
| ASK | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.02% | **+1.61%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| ASK_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 52件 (TP 19 / SL 32 / EXP 1)
- 最新: TAIKO/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2206件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 556件 (Win 136 / Loss 131 / Flat 289) / skip 944件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T14:43:45.068614+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.82% price=61406.3
- Funnel: target 834 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +92.80% | $18,599,110.62 |
| BIRB/USDT:USDT | +66.88% | $9,004,221.14 |
| M/USDT:USDT | +44.01% | $6,121,387.10 |
| US/USDT:USDT | +31.52% | $2,283,712.05 |
| BREV/USDT:USDT | +25.24% | $6,228,910.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +3.67% | +4.49% |
| BEAT/USDT:USDT | below_1h_threshold | +1.99% | +2.81% |
| BIRB/USDT:USDT | below_1h_threshold | +1.82% | +2.64% |
| B/USDT:USDT | below_1h_threshold | +0.74% | +1.56% |
| BANK/USDT:USDT | below_1h_threshold | +0.59% | +1.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
