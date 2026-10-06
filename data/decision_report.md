# Decision Report

- generated_at: 2026-10-06T12:26:56.560538+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16207**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16207, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +3.45% | **+0.69%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 9/16 | 56.2% | -0.29% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.04% | **+3.04%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.12% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,322.89** / 初期 $100.00 (+1222.89%)
- 確定: 6249件 (Win 1833 / Loss 1998 / Flat 2418) / skip 6519件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,322.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.55** / 初期 $100.00 (+176.55%)
- 確定: 3616件 (Win 1007 / Loss 846 / Flat 1763) / skip 6002件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $276.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T12:26:35.120422+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=86113.9
- Funnel: target 1074 → liquid 174 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +79.74% | $38,415,232.98 |
| US/USDT:USDT | +45.13% | $1,340,769.23 |
| BR/USDT:USDT | +33.19% | $46,597,541.99 |
| NMR/USDT:USDT | +29.58% | $6,352,118.58 |
| ORCA/USDT:USDT | +27.95% | $3,511,828.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OKB/USDT:USDT | below_1h_threshold | +4.53% | +4.64% |
| ORDI/USDT:USDT | below_1h_threshold | +3.12% | +3.23% |
| BR/USDT:USDT | below_1h_threshold | +2.80% | +2.91% |
| GRASS/USDT:USDT | below_1h_threshold | +2.39% | +2.51% |
| AVAX/USDT:USDT | below_1h_threshold | +1.28% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
