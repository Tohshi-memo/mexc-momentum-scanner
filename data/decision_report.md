# Decision Report

- generated_at: 2026-09-02T21:46:46.687628+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13388**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13388, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_BB3S | 4/16 | 25.0% | +0.15% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.42% | **-0.14%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |
| LIMIT_10PCT | 2/20 | 10.0% | -4.00% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.64% | **+1.45%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.81% | **+1.44%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.44%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.36% | **+1.18%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$879.08** / 初期 $100.00 (+779.08%)
- 確定: 4992件 (Win 1514 / Loss 1636 / Flat 1842) / skip 4957件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $879.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$187.86** / 初期 $100.00 (+87.86%)
- 確定: 2367件 (Win 671 / Loss 571 / Flat 1125) / skip 4432件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1652 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $187.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.17** / 初期 $100.00 (+15.17%)
- 確定: 2102件 (Win 614 / Loss 822 / Flat 666) / pending 6件 / skip 2759件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000509 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $115.17

## 6. Latest Market Context

- 更新: 2026-09-02T21:46:28.024888+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=77330.8
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 7 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.4 >= 65=1, 4h RSI 77.5 >= 65=1, 4h RSI 84.0 >= 65=1, 4h RSI 93.9 >= 65=1, 4h RSI 73.1 >= 65=1, 4h RSI 88.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +194.90% | $57,966,938.64 |
| BTW/USDT:USDT | +39.29% | $8,642,054.37 |
| BULLA/USDT:USDT | +32.23% | $3,102,624.72 |
| SNOWSTOCK/USDT:USDT | +21.24% | $1,309,305.10 |
| BONER/USDT:USDT | +17.44% | $2,325,878.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +4.20% | +4.24% |
| BONER/USDT:USDT | below_1h_threshold | +3.60% | +3.65% |
| HEMI/USDT:USDT | below_1h_threshold | +2.05% | +2.10% |
| CRV/USDT:USDT | below_1h_threshold | +1.95% | +2.00% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.53% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
