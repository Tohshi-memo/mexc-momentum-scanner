# Decision Report

- generated_at: 2026-11-11T05:51:27.798705+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18647**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18647, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.47% | **+0.74%** |
| LIMIT_ATR | 4/20 | 20.0% | +1.51% | **+0.30%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.21% | **+0.15%** |
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_4PCT | 9/20 | 45.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.14% | **+1.18%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.66% | **+1.16%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.96% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 269件 (TP 97 / SL 164 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7210件 (Win 2073 / Loss 2305 / Flat 2832) / skip 7998件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7280件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0101 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6806件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000501 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T05:51:12.127892+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=73871.9
- Funnel: target 1099 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +41.99% | $18,131,286.34 |
| MUU/USDT:USDT | +15.82% | $14,176,158.08 |
| FLOAT/USDT:USDT | +15.69% | $1,107,372.14 |
| CRWVSTOCK/USDT:USDT | +14.79% | $5,872,514.51 |
| KORU/USDT:USDT | +14.58% | $128,145,054.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +1.39% | +1.16% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.19% | +0.96% |
| SNXX/USDT:USDT | below_1h_threshold | +0.80% | +0.57% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +0.78% | +0.55% |
| PYTH/USDT:USDT | below_1h_threshold | +0.69% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
