# Decision Report

- generated_at: 2026-11-19T18:11:26.622940+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19211**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19211, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.62% | **+0.16%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.29% | **+1.03%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.53% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,692.99** / 初期 $100.00 (+1592.99%)
- 確定: 7381件 (Win 2119 / Loss 2376 / Flat 2886) / skip 8391件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANTHROPIC/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,692.99

## 4. Robust Adaptive DryRun ($100)

- 残高: **$432.52** / 初期 $100.00 (+332.52%)
- 確定: 5036件 (Win 1341 / Loss 1087 / Flat 2608) / skip 7586件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0030 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $432.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7375件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-19T18:11:13.333316+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=62713.1
- Funnel: target 1084 → liquid 148 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ICNT/USDT:USDT | +9.94% | $4,549,028.91 |
| SOXS/USDT:USDT | +8.85% | $48,033,893.33 |
| UVXY/USDT:USDT | +7.18% | $2,172,131.39 |
| MMT/USDT:USDT | +5.97% | $8,346,980.55 |
| SQQQ/USDT:USDT | +5.32% | $9,035,992.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UVXY/USDT:USDT | below_1h_threshold | +2.14% | +2.16% |
| MMT/USDT:USDT | below_1h_threshold | +2.12% | +2.14% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.82% |
| SOXS/USDT:USDT | below_1h_threshold | +1.72% | +1.75% |
| SQQQ/USDT:USDT | below_1h_threshold | +1.31% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
