# Decision Report

- generated_at: 2026-07-13T18:06:14.290868+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8647**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8647, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.76% | **+0.97%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | +0.85% | **+0.21%** |
| LIMIT_BB3S | 4/20 | 20.0% | +0.02% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +4.31% | **+2.37%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.66% | **+2.19%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.20% | **+2.08%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.69% | **+1.64%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$101.19** / 初期 $100.00 (+1.19%)
- 確定トレード: 94件 (TP 31 / SL 61 / EXP 2)
- 最新: AIOT/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$328.48** / 初期 $100.00 (+228.48%)
- 確定: 2815件 (Win 886 / Loss 923 / Flat 1006) / skip 2393件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $328.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.26** / 初期 $100.00 (+5.26%)
- 確定: 648件 (Win 154 / Loss 159 / Flat 335) / skip 1410件
- 成長率目線: 平均log +0.000079 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0164 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIOT/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $105.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.48** / 初期 $100.00 (-0.52%)
- 確定: 39件 (Win 14 / Loss 25 / Flat 0) / pending 0件 / skip 78件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000303 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $99.48

## 6. Latest Market Context

- 更新: 2026-07-13T18:06:06.863894+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=62008.2
- Funnel: target 867 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +23.62% | $19,927,741.59 |
| AIOT/USDT:USDT | +21.73% | $2,640,745.08 |
| ALLO/USDT:USDT | +10.93% | $24,299,240.84 |
| VELVET/USDT:USDT | +3.64% | $28,140,716.45 |
| USOIL/USDT:USDT | +3.50% | $96,783,063.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +2.38% | +2.18% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.31% | +2.10% |
| AIOT/USDT:USDT | below_1h_threshold | +2.11% | +1.91% |
| XPL/USDT:USDT | below_1h_threshold | +1.66% | +1.45% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.24% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
