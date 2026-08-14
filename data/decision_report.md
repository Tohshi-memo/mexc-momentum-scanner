# Decision Report

- generated_at: 2026-08-14T22:06:22.708326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11609**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11609, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 8/20 | 40.0% | +3.36% | **+1.34%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +4.19% | **+1.05%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.53% | **+1.01%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.70% | **+0.94%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.97% | **+0.74%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$635.36** / 初期 $100.00 (+535.36%)
- 確定: 4077件 (Win 1277 / Loss 1342 / Flat 1458) / skip 4093件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $635.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.02** / 初期 $100.00 (+52.02%)
- 確定: 1673件 (Win 479 / Loss 404 / Flat 790) / skip 3347件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0569 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $152.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1557件 (Win 473 / Loss 597 / Flat 487) / pending 3件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-14T22:06:14.252551+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62917.6
- Funnel: target 985 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +27.81% | $6,718,616.43 |
| ACE/USDT:USDT | +20.78% | $67,417,676.97 |
| DOLO/USDT:USDT | +17.06% | $1,592,483.58 |
| ACU/USDT:USDT | +10.28% | $1,836,269.41 |
| CAP/USDT:USDT | +8.69% | $20,849,697.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOLO/USDT:USDT | below_1h_threshold | +1.74% | +1.71% |
| SNXX/USDT:USDT | below_1h_threshold | +1.60% | +1.57% |
| ACU/USDT:USDT | below_1h_threshold | +1.57% | +1.54% |
| CAP/USDT:USDT | below_1h_threshold | +1.11% | +1.08% |
| US/USDT:USDT | below_1h_threshold | +1.05% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
