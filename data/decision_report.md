# Decision Report

- generated_at: 2026-09-05T17:41:31.757258+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13763**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13763, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.10% | **-1.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.77% | **+0.31%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_ATR | 15/20 | 75.0% | -0.20% | **-0.15%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.41% | **+1.06%** |
| MARKET_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.85% | **+0.93%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.68% | **+0.93%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.05% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.61** / 初期 $100.00 (+755.61%)
- 確定: 5069件 (Win 1521 / Loss 1653 / Flat 1895) / skip 5255件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $855.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.66** / 初期 $100.00 (+88.66%)
- 確定: 2508件 (Win 699 / Loss 591 / Flat 1218) / skip 4666件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0482 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $188.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.64** / 初期 $100.00 (+19.64%)
- 確定: 2383件 (Win 707 / Loss 904 / Flat 772) / pending 3件 / skip 2850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000238 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.64

## 6. Latest Market Context

- 更新: 2026-09-05T17:41:16.890280+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79976.2
- Funnel: target 1050 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +17.04% | $24,688,196.22 |
| NIULAI/USDT:USDT | +16.41% | $2,566,026.91 |
| MAGMA/USDT:USDT | +13.82% | $2,185,206.57 |
| USELESS/USDT:USDT | +10.14% | $20,657,549.99 |
| BASECAT/USDT:USDT | +8.18% | $2,023,178.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.47% | +4.51% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.18% | +3.21% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.57% | +2.60% |
| B/USDT:USDT | below_1h_threshold | +2.09% | +2.12% |
| LIT/USDT:USDT | below_1h_threshold | +1.78% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
