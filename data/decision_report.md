# Decision Report

- generated_at: 2026-06-17T00:58:51.420294+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6890**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6890, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.35% | **+0.47%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 4/18 | 22.2% | -1.72% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$187.29** / 初期 $100.00 (+87.29%)
- 確定: 1763件 (Win 467 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $187.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.82** / 初期 $100.00 (-2.18%)
- 確定: 163件 (Win 31 / Loss 31 / Flat 101) / skip 138件
- 成長率目線: 平均log -0.000135 / 幾何平均 -0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0390 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $97.82

## 5. Latest Market Context

- 更新: 2026-06-17T00:58:44.774624+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=65727.7
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +34.71% | $5,167,111.91 |
| SQD/USDT:USDT | +20.86% | $1,238,396.47 |
| VELVET/USDT:USDT | +19.20% | $30,737,402.01 |
| H/USDT:USDT | +17.17% | $56,355,792.25 |
| ESPORTS/USDT:USDT | +15.89% | $2,286,887.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.70% | +4.57% |
| SQD/USDT:USDT | below_1h_threshold | +4.43% | +4.30% |
| UNI/USDT:USDT | below_1h_threshold | +4.01% | +3.88% |
| PLAY/USDT:USDT | below_1h_threshold | +3.29% | +3.17% |
| VVV/USDT:USDT | below_1h_threshold | +3.01% | +2.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
