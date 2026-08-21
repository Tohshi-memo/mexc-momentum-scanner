# Decision Report

- generated_at: 2026-08-21T00:51:41.480466+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12112**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12112, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_BB3S_LONG | 4/7 | 57.1% | +2.21% | **+1.26%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.81% | **+0.61%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.81% | **+0.48%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$642.10** / 初期 $100.00 (+542.10%)
- 確定: 4323件 (Win 1325 / Loss 1415 / Flat 1583) / skip 4350件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $642.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3701件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0855 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.66** / 初期 $100.00 (+17.66%)
- 確定: 1798件 (Win 534 / Loss 681 / Flat 583) / pending 5件 / skip 1782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000247 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.66

## 6. Latest Market Context

- 更新: 2026-08-21T00:51:29.976906+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.96% price=73694.1
- Funnel: target 1011 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +53.43% | $3,456,734.63 |
| ONG/USDT:USDT | +52.43% | $20,507,487.85 |
| ONT/USDT:USDT | +20.55% | $3,319,769.67 |
| ENA/USDT:USDT | +15.43% | $45,922,452.48 |
| BTW/USDT:USDT | +14.00% | $90,141,298.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_relative_strength | +5.71% | +4.74% |
| ONT/USDT:USDT | below_1h_threshold | +4.08% | +3.11% |
| CHIP/USDT:USDT | below_1h_threshold | +3.15% | +2.19% |
| BTW/USDT:USDT | below_1h_threshold | +3.07% | +2.11% |
| TUT/USDT:USDT | below_1h_threshold | +3.02% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
