# Decision Report

- generated_at: 2026-08-08T17:01:17.231262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10868**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10868, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.39% | **-1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.80% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.00% | **+2.40%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +2.22% | **+1.85%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.29% | **+1.71%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.78% | **+1.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$653.20** / 初期 $100.00 (+553.20%)
- 確定: 3869件 (Win 1220 / Loss 1258 / Flat 1391) / skip 3560件
- 成長率目線: 平均log +0.000485 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $653.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2768件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0435 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.76** / 初期 $100.00 (+18.76%)
- 確定: 1234件 (Win 389 / Loss 473 / Flat 372) / pending 6件 / skip 1102件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000242 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.76

## 6. Latest Market Context

- 更新: 2026-08-08T17:01:09.734655+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=65057.7
- Funnel: target 961 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +14.11% | $14,729,294.22 |
| TUT/USDT:USDT | +8.80% | $14,285,754.72 |
| TAKE/USDT:USDT | +6.50% | $1,051,061.18 |
| BLUAI/USDT:USDT | +2.78% | $4,688,801.35 |
| BANK/USDT:USDT | +2.03% | $2,981,036.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +1.38% | +1.38% |
| ICP/USDT:USDT | below_1h_threshold | +0.55% | +0.55% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.39% | +0.39% |
| SOXL/USDT:USDT | below_1h_threshold | +0.29% | +0.29% |
| USOIL/USDT:USDT | below_1h_threshold | +0.26% | +0.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
