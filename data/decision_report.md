# Decision Report

- generated_at: 2026-11-21T15:41:34.961188+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19315**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19315, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.90% | **+1.81%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.78% | **+1.51%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.19% | **+1.09%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.07% | **+1.03%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.34% | **+2.00%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.77% | **+1.66%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.58%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,703.43** / 初期 $100.00 (+1603.43%)
- 確定: 7458件 (Win 2141 / Loss 2401 / Flat 2916) / skip 8418件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $1,703.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$451.38** / 初期 $100.00 (+351.38%)
- 確定: 5120件 (Win 1363 / Loss 1098 / Flat 2659) / skip 7606件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0384 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $451.38

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7475件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T15:41:17.471568+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.76% price=59857.8
- Funnel: target 1086 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +73.24% | $1,291,010.43 |
| SKYAI/USDT:USDT | +26.99% | $1,027,636.16 |
| IDOL/USDT:USDT | +25.15% | $1,721,889.32 |
| VVV/USDT:USDT | +16.87% | $5,283,356.76 |
| RARE/USDT:USDT | +16.18% | $8,171,374.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IDOL/USDT:USDT | below_1h_threshold | +4.77% | +5.53% |
| BTW/USDT:USDT | below_1h_threshold | +2.40% | +3.15% |
| SOXS/USDT:USDT | below_1h_threshold | +2.12% | +2.88% |
| DODO/USDT:USDT | below_1h_threshold | +1.22% | +1.97% |
| SPX/USDT:USDT | below_1h_threshold | +0.77% | +1.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
