# Decision Report

- generated_at: 2026-08-19T11:31:16.000464+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11972**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11972, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |
| LIMIT_3PCT | 13/20 | 65.0% | -0.17% | **-0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.58% | **+0.09%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.13% | **+0.04%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | -0.15% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$622.90** / 初期 $100.00 (+522.90%)
- 確定: 4233件 (Win 1301 / Loss 1381 / Flat 1551) / skip 4300件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $622.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3562件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0349 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.79** / 初期 $100.00 (+17.79%)
- 確定: 1749件 (Win 520 / Loss 665 / Flat 564) / pending 1件 / skip 1691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000138 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.79

## 6. Latest Market Context

- 更新: 2026-08-19T11:31:07.483665+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=64477.6
- Funnel: target 992 → liquid 178 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +65.29% | $93,463,589.68 |
| HEMI/USDT:USDT | +34.70% | $3,580,358.72 |
| UNITREE/USDT:USDT | +22.48% | $16,600,131.47 |
| DOS/USDT:USDT | +16.87% | $1,166,351.45 |
| NIULAI/USDT:USDT | +14.25% | $4,538,525.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +1.90% | +1.82% |
| CAP/USDT:USDT | below_1h_threshold | +1.84% | +1.76% |
| RE/USDT:USDT | below_1h_threshold | +1.37% | +1.28% |
| UNI/USDT:USDT | below_1h_threshold | +1.24% | +1.15% |
| KORU/USDT:USDT | below_1h_threshold | +1.14% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
