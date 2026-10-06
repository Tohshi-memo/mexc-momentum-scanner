# Decision Report

- generated_at: 2026-10-06T12:11:39.479862+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16204**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16204, expectancy=+0.00%
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
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +3.16% | **+0.63%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 7/15 | 46.7% | -0.28% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.44% | **+3.44%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.89% | **+2.02%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +3.58% | **+1.61%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.07% | **+0.73%** |
| LIMIT_3PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,329.57** / 初期 $100.00 (+1229.57%)
- 確定: 6246件 (Win 1832 / Loss 1996 / Flat 2418) / skip 6519件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OKB/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $1,329.57

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.34** / 初期 $100.00 (+176.34%)
- 確定: 3613件 (Win 1006 / Loss 845 / Flat 1762) / skip 6002件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0212 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: OKB/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $276.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4369件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000065 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T12:11:25.028812+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=86257.6
- Funnel: target 1074 → liquid 174 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +86.27% | $37,571,108.83 |
| US/USDT:USDT | +47.71% | $1,304,798.00 |
| ORCA/USDT:USDT | +30.13% | $3,489,592.75 |
| BR/USDT:USDT | +29.65% | $45,472,694.39 |
| NMR/USDT:USDT | +28.49% | $5,667,644.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +4.13% | +4.08% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.96% | +3.91% |
| AVAX/USDT:USDT | below_1h_threshold | +2.19% | +2.13% |
| SOXL/USDT:USDT | below_1h_threshold | +1.09% | +1.04% |
| VELVET/USDT:USDT | below_1h_threshold | +0.98% | +0.93% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
