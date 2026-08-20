# Decision Report

- generated_at: 2026-08-20T19:51:39.373380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12077**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12077, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT | 6/20 | 30.0% | +3.40% | **+1.02%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.10% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.65% | **+1.99%** |
| MARKET_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +2.10% | **+1.17%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.70% | **+0.94%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.69% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$615.13** / 初期 $100.00 (+515.13%)
- 確定: 4290件 (Win 1312 / Loss 1402 / Flat 1576) / skip 4348件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $615.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3666件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0648 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.73** / 初期 $100.00 (+16.73%)
- 確定: 1770件 (Win 526 / Loss 675 / Flat 569) / pending 5件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000116 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $116.73

## 6. Latest Market Context

- 更新: 2026-08-20T19:51:24.043845+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=72654.1
- Funnel: target 1011 → liquid 199 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +39.50% | $2,268,138.48 |
| ONG/USDT:USDT | +15.50% | $4,955,806.64 |
| PEOPLE/USDT:USDT | +14.04% | $2,520,670.04 |
| TUT/USDT:USDT | +11.72% | $5,010,945.43 |
| ALLO/USDT:USDT | +8.66% | $4,503,676.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEOPLE/USDT:USDT | below_1h_threshold | +4.22% | +3.86% |
| TURBO/USDT:USDT | below_1h_threshold | +3.60% | +3.25% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.29% | +2.94% |
| AKE/USDT:USDT | below_1h_threshold | +2.60% | +2.24% |
| HEI/USDT:USDT | below_1h_threshold | +2.03% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
