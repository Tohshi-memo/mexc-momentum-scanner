# Decision Report

- generated_at: 2026-08-21T03:21:48.990683+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12137**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12137, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.51% | **+0.75%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.36% | **+2.01%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.41% | **+1.02%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.14% | **+0.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.54% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$659.91** / 初期 $100.00 (+559.91%)
- 確定: 4348件 (Win 1336 / Loss 1427 / Flat 1585) / skip 4350件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRV/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $659.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3726件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0710 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.41** / 初期 $100.00 (+17.41%)
- 確定: 1821件 (Win 540 / Loss 690 / Flat 591) / pending 3件 / skip 1789件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000173 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.41

## 6. Latest Market Context

- 更新: 2026-08-21T03:21:30.776099+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=74460.0
- Funnel: target 1011 → liquid 194 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 73.5 >= 65=1, 4h RSI 69.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +112.75% | $4,564,748.85 |
| ONG/USDT:USDT | +95.63% | $33,424,251.94 |
| ONT/USDT:USDT | +25.65% | $3,667,555.92 |
| ENA/USDT:USDT | +19.83% | $54,504,481.71 |
| BTW/USDT:USDT | +17.39% | $86,108,388.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +3.08% | +3.02% |
| KORU/USDT:USDT | below_1h_threshold | +2.02% | +1.96% |
| NIL/USDT:USDT | below_1h_threshold | +1.91% | +1.85% |
| MVLL/USDT:USDT | below_1h_threshold | +1.78% | +1.71% |
| AKE/USDT:USDT | below_1h_threshold | +1.65% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
