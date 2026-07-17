# Decision Report

- generated_at: 2026-07-17T19:06:11.423635+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8879**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8879, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.43% | **-1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.62% | **+0.22%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_6PCT_LONG | 5/20 | 25.0% | +3.95% | **+0.99%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.37% | **+0.83%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.14% | **+0.80%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$361.13** / 初期 $100.00 (+261.13%)
- 確定: 2994件 (Win 932 / Loss 952 / Flat 1110) / skip 2446件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $361.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.59** / 初期 $100.00 (+10.59%)
- 確定: 841件 (Win 199 / Loss 172 / Flat 470) / skip 1449件
- 成長率目線: 平均log +0.000120 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1350 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $110.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.52** / 初期 $100.00 (-0.48%)
- 確定: 140件 (Win 45 / Loss 76 / Flat 19) / pending 3件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000402 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.52

## 6. Latest Market Context

- 更新: 2026-07-17T19:06:03.710195+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=64149.6
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +32.55% | $9,360,286.84 |
| CASHCAT/USDT:USDT | +16.53% | $1,173,280.10 |
| AKE/USDT:USDT | +11.28% | $34,398,028.97 |
| GALA/USDT:USDT | +7.27% | $1,922,525.29 |
| VVV/USDT:USDT | +6.60% | $2,240,736.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.99% | +5.11% |
| CASHCAT/USDT:USDT | below_1h_threshold | +1.83% | +1.95% |
| ANSEM/USDT:USDT | below_1h_threshold | +1.78% | +1.90% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.20% | +1.31% |
| SOXS/USDT:USDT | below_1h_threshold | +1.16% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
