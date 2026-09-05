# Decision Report

- generated_at: 2026-09-05T14:36:27.708836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13739**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13739, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.19% | **-0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.36% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.12% | **+1.80%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.26% | **+1.47%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.30% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 204件 (TP 76 / SL 123 / EXP 5)
- 最新: CP/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$857.40** / 初期 $100.00 (+757.40%)
- 確定: 5045件 (Win 1519 / Loss 1649 / Flat 1877) / skip 5255件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $857.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$189.70** / 初期 $100.00 (+89.70%)
- 確定: 2484件 (Win 697 / Loss 587 / Flat 1200) / skip 4666件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0884 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $189.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.33** / 初期 $100.00 (+19.33%)
- 確定: 2364件 (Win 704 / Loss 901 / Flat 759) / pending 4件 / skip 2844件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` TP_HIT account +0.34% 残高後 $119.33

## 6. Latest Market Context

- 更新: 2026-09-05T14:36:15.116623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=79706.7
- Funnel: target 1050 → liquid 134 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1, 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +104.75% | $16,023,971.23 |
| 4/USDT:USDT | +64.12% | $21,818,314.87 |
| BASECAT/USDT:USDT | +39.58% | $1,880,151.24 |
| ICX/USDT:USDT | +38.61% | $1,120,021.30 |
| AKE/USDT:USDT | +36.59% | $19,646,591.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +4.53% | +4.37% |
| PONS/USDT:USDT | below_1h_threshold | +3.74% | +3.57% |
| CHIP/USDT:USDT | below_1h_threshold | +2.47% | +2.30% |
| USELESS/USDT:USDT | below_1h_threshold | +1.89% | +1.72% |
| ICX/USDT:USDT | below_1h_threshold | +1.52% | +1.35% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
